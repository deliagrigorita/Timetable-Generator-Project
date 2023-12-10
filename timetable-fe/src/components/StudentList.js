import React, { Component } from "react";
import { Table } from "reactstrap";
import NewStudentModal from "./NewStudentModal";
import ConfirmRemovalModal from "./ConfirmRemovalModal";
import api from "../constants/api";  

class StudentList extends Component {
  componentDidMount() {
    // Fetch data when the component mounts
    this.handleGetAll();
  }

  handleGetAll = async () => {
    try {
      // Make a GET request to fetch all students
      const response = await api.get("students");
      // Update the state with the fetched data
      this.props.resetState(response.data);
    } catch (error) {
      console.error("Error fetching students:", error);
    }
  };

  render() {
    const students = this.props.students;

    return (
      <Table dark>
        <thead>
          <tr>
            <th>Last Name</th>
            <th>First Name</th>
            <th>Email</th>
            <th>Password</th>
            <th>Data of birth</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!students || students.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            students.map((student) => (
              <tr key={student.pk}>
                <td>{student.last_name}</td>
                <td>{student.first_name}</td>
                <td>{student.email}</td>
                <td>{student.password}</td>
                <td>{student.date_of_birth}</td>
                <td align="center">
                  <NewStudentModal
                    create={false}
                    student={student}
                    resetState={this.handleGetAll}
                  />
                  &nbsp;&nbsp;
                  {/* Delete button removed */}
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default StudentList;