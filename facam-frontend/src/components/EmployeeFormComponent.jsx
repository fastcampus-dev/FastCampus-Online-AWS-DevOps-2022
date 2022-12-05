import React, { Component } from "react";
import EmployeeService from "../services/EmployeeService";

export default class EmployeeFormComponent extends Component {

  constructor(props) {
    super(props);

    this.state = {
      id: this.props.match.params.id,
      firstName: "",
      lastName: "",
      emailAddress: "",
    };

    this.changeFirstNameHandler = this.changeFirstNameHandler.bind(this);
    this.changeLastNameHandler = this.changeLastNameHandler.bind(this);
    this.changeEmailHandler = this.changeEmailHandler.bind(this);
    this.saveEmployee = this.saveEmployee.bind(this);
    this.cancelSave = this.cancelSave.bind(this);
  }

  // get employee by id to update
  componentDidMount() {
    if (this.state.id === undefined) {
      return;
    } else {
      EmployeeService.getEmployeeById(this.state.id).then((res) => {

        let employee = res.data;

        console.log(JSON.stringify(employee));
        this.setState({
          firstName: employee.firstName,
          lastName: employee.lastName,
          emailAddress: employee.emailAddress,
        });
      });
    }
  }


  // save or update employee
  saveEmployee = (e) => {
    e.preventDefault();
    let employee = {
      id: this.state.id,
      firstName: this.state.firstName,
      lastName: this.state.lastName,
      emailAddress: this.state.emailAddress,
    };
    console.log("Employee:" + JSON.stringify(employee));
    if (this.state.id === undefined) {
      EmployeeService.addEmployee(employee).then((res) => {
//         res.header('Access-Control-Allow-Origin', '*');
//         res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
//         res.header('Access-Control-Allow-Headers',
//         'Content-Type, Authorization, Content-Length, X-Requested-With');
        this.props.history.push("/employees");
      });
    } else {
      EmployeeService.updateEmployee(employee).then((res) => {
        this.props.history.push("/employees");
      });
    }
  };

  cancelSave() {
    this.props.history.push("/employees");
  }

  changeFirstNameHandler(event) {
    this.setState({ firstName: event.target.value });
  }

  changeLastNameHandler(event) {
    this.setState({ lastName: event.target.value });
  }

  changeEmailHandler(event) {
    this.setState({ emailAddress: event.target.value });
  }

  getTitle() {
    if (this.state.id === undefined) {
      return (
        <div>
          <h2 className="text-center">Add Employee</h2>
        </div>
      );
    } else {
      return (
        <div>
          <h2 className="text-center">Update Employee</h2>
        </div>
      );
    }
  }

  render() {
    return (
      <div>
        <div className="container">
          <div className="row">
            <div
              className="card col-md-6 offset-md-3 offset-md-3"
              style={{ marginTop: "10px" }}
            >
              {this.getTitle()}
              <form>
                <div className="form-group">
                  <label>First Name:</label>
                  <input
                    placeholder="First Name"
                    name="firstName"
                    className="form-control"
                    value={this.state.firstName}
                    onChange={this.changeFirstNameHandler}
                  />

                  <label>Last Name:</label>
                  <input
                    placeholder="Last Name"
                    name="lastName"
                    className="form-control"
                    value={this.state.lastName}
                    onChange={this.changeLastNameHandler}
                  />

                  <label>Email Address:</label>
                  <input
                    placeholder="Email Address"
                    name="emailAddress"
                    className="form-control"
                    value={this.state.emailAddress}
                    onChange={this.changeEmailHandler}
                  />
                </div>
                <button className="btn btn-success" onClick={this.saveEmployee}>
                  Save
                </button>
                <button
                  className="btn btn-danger"
                  onClick={this.cancelSave}
                  style={{ marginLeft: "10px" }}
                >
                  Cancel
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
