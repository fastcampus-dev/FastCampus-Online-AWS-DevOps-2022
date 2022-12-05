package com.kimdragon.employeemanagement.service;

import com.kimdragon.employeemanagement.domain.Employee;

import java.util.List;

public interface IEmployeeService {
    Employee add(Employee employee);

    List<Employee> getAll();

    Employee update(Employee employee);

    void delete(Employee employee);

    Employee findById(Long id);

    void deleteById(Long id);
}
