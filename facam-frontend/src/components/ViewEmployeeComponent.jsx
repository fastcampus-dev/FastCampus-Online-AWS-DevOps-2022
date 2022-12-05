import React, { Component } from "react";
import EmployeeService from "../services/EmployeeService";

export default class ViewEmployeeComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      id: this.props.match.params.id,
      employee: {},
    };
  }
  //get data by id and assign to employee state object
  componentDidMount() {
    EmployeeService.getEmployeeById(this.state.id).then((res) => {
      this.setState({ employee: res.data });
    });
  }
  render() {
    return (
      <div>
        <div
          className="card col-md-6 offset-md-3"
          style={{ marginTop: "10px" }}
        >
          <h2 className="text-center"> View Employee Details</h2>
          <div className="card-body">
            <div className="row">
              <label style={{ fontWeight: "bold" }}>
                Employee First Name:{" "}
              </label>
              <div>{this.state.employee.firstName}</div>
            </div>
            <div className="row">
              <label style={{ fontWeight: "bold" }}>Employee Last Name: </label>
              <div>{this.state.employee.lastName}</div>
            </div>
            <div className="row">
              <label style={{ fontWeight: "bold" }}>
                Employee Email Address:{" "}
              </label>
              <div>{this.state.employee.emailAddress}</div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
