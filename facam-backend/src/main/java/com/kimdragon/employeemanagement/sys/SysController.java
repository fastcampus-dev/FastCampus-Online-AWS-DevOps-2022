package com.kimdragon.employeemanagement.sys;

import org.aspectj.bridge.MessageUtil;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/sys")
public class SysController {

    private MessageUtil logger;

    // healthz check
    @GetMapping("/healthz")
    public String healthz() {
        logger.debug("########################healthz");
        return "UP";
    }

}
