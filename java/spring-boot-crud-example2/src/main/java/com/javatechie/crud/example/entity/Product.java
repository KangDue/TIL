package com.javatechie.crud.example.entity;

import com.javatechie.crud.example.service.ImgService;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import com.javatechie.crud.example.common.CommonMethods;
@Data
@RequiredArgsConstructor
@Entity
@Table(name = "product")
public class Product {
    @Id
    @GeneratedValue
    @Column(name = "product_id")
    private int id;
    @Column(name = "product_name")
    private String name;

    @OneToMany(mappedBy="product")
    private List<Img> imgList = new ArrayList<>();;
    private int quantity; // count 대신
    private int price;
    private String description;

    private int category_id; // category

}
