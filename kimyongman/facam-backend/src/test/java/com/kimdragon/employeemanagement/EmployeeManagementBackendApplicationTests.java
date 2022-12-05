package com.kimdragon.employeemanagement;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


@SpringBootTest
class EmployeeManagementBackendApplicationTests {

    private final Logger logger = LoggerFactory.getLogger(this.getClass());

    @Test
    void contextLoads() {
            System.out.print("Hello world");
            logger.info("Hello world");
    }

}
