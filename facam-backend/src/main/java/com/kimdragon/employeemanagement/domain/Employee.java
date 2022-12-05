package com.kimdragon.employeemanagement.domain;

import io.swagger.annotations.ApiModel;

import javax.persistence.*;

@Entity
@Table(name = "employee")
@ApiModel
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    private String firstName;
    private String lastName;
    private String emailAddress;

    public Employee() {

    }
    public Employee(String firstName, String lastName, String emailAddress) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.emailAddress = emailAddress;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmailAddress() {
        return emailAddress;
    }

    public void setEmailAddress(String eMail) {
        this.emailAddress = eMail;
    }
}
