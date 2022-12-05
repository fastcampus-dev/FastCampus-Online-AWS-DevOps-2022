package com.kimdragon.employeemanagement.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@Configuration
@EnableSwagger2
public class SwaggerConfig  implements WebMvcConfigurer {
    @SuppressWarnings("desprecation")
    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("TEST EMP API")
                .description("Spring Boot - GSN SA TEST EMP API")
                .version("V1")
                .build();
    }

    @Bean
    public Docket api() {
        String version = "V1";
        return new Docket(DocumentationType.SWAGGER_2)
                .useDefaultResponseMessages(false)
                .apiInfo(apiInfo())
                .groupName(version)
                .select()
                .apis(RequestHandlerSelectors.any())
                .paths(PathSelectors.ant("/api/v1/employees/**"))
                .build();
    }

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOrigins("*")
                .allowedMethods("*");
    }
}