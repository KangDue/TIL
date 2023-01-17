package com.javatechie.crud.example.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;

import javax.persistence.*;

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

    private String imgUrl;
    private int quantity; // count 대신
    private int price;
    private String description;

    private int category_id; // category
}
