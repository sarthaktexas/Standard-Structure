package com.example.basic.controller;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

//flags class as restcontroller
@RestController
public class MainController {
    //flags function as a request map, and maps it to /
	@RequestMapping("/")
	public String index() {
		return "Hello World";
	}
}