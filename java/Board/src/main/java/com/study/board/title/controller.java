package com.study.board.title;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class controller {
    @GetMapping("/v1")
    public String test1() {
        return "v1";
    }
}
