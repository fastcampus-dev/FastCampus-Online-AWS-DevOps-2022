package com.kimdragon.employeemanagement.controller;

import com.kimdragon.employeemanagement.domain.Employee;
import com.kimdragon.employeemanagement.service.IEmployeeService;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/v1/")
@CrossOrigin()

class EmployeeController {

    private final Logger logger = LoggerFactory.getLogger(this.getClass());


    @Autowired
    private IEmployeeService employeeService;

    //get all employees
    @GetMapping("/employees")
    @ApiOperation(value ="emp list", notes = "회원 리스트")

    public List<Employee> getAll() {

        logger.debug("employee_list");

        return employeeService.getAll();


    }

    //add employee
    @PostMapping("/employees")
    @ApiOperation(value ="emp Add", notes = "회원 추가")
    public Employee createEmployee(@RequestBody Employee employee) {

        logger.debug("employee_add");

        return employeeService.add(employee);
    }

    //get employee by id
    @GetMapping("/employees/{id}")
    @ApiOperation(value ="emp Get", notes = "회원정보 확인")
    @ApiImplicitParam(name = "id", value = "ID", required = true, dataType = "string", paramType = "path")

    public ResponseEntity<Employee> getById(@PathVariable Long id) {

        logger.debug("employee_getid");

        Employee employee = employeeService.findById(id);
        return ResponseEntity.ok(employee);
    }

    //update employee
    @PutMapping("/employees")
    @ApiOperation(value ="emp Update", notes = "회원 업데이트")

    public ResponseEntity<Employee> update(@RequestBody Employee employee) {

        logger.debug("employee_update");

        Employee employeeUpdated = employeeService.update(employee);
        return ResponseEntity.ok(employeeUpdated);
    }

    //delete employee
    @PostMapping("/employees/delete")
    @ApiOperation(value ="emp Delete", notes = "회원 삭제")

    public ResponseEntity<String> delete(@RequestBody Employee employee) {

        logger.debug("employee_delete ");

        employeeService.delete(employee);
        return ResponseEntity.ok("Employee deleted.");
    }

    // deleteById
    @DeleteMapping("employees/{id}")
    @ApiOperation(value ="emp Delete Byid", notes = "회원 삭제")
    @ApiImplicitParam(name = "id", value = "ID", required = true, dataType = "string", paramType = "path")

    public ResponseEntity<Map<String,Boolean>> deleteById(@PathVariable Long id){

        logger.debug("employee_delete_byid");

        employeeService.deleteById(id);
        Map<String,Boolean> response = new HashMap<>();
        response.put("Deleted", Boolean.TRUE);
        return  ResponseEntity.ok(response);
    }

    @GetMapping("/healthz")
    public String healthz() {
        logger.debug("########################healthz");
        return "UP";
    }



}
