import "./App.css";
import FooterComponent from "./components/FooterComponent";
import HeaderComponent from "./components/HeaderComponent";
import ListEmployeeComponent from "./components/ListEmployeeComponent";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import EmployeeFormComponent from "./components/EmployeeFormComponent";
import ViewEmployeeComponent from "./components/ViewEmployeeComponent";

function App() {
  return (
    <div>
      <Router>
        <HeaderComponent />
        <div className="container">
          <Switch>
            <Route path="/" exact component={ListEmployeeComponent}></Route>
            <Route path="/employees" component={ListEmployeeComponent}></Route>
            <Route
              path="/add-employee"
              component={EmployeeFormComponent}
            ></Route>
            <Route
              path="/update-employee/:id"
              component={EmployeeFormComponent}
            ></Route>
            <Route
              path="/view-employee/:id"
              component={ViewEmployeeComponent}
            ></Route>
          </Switch>
        </div>
        <FooterComponent />
      </Router>
    </div>
  );
}

export default App;
