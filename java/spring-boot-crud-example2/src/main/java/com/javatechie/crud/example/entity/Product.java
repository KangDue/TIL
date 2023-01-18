package com.javatechie.crud.example.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.javatechie.crud.example.service.ImgService;
import lombok.*;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import com.javatechie.crud.example.common.CommonMethods;
@Setter
@Getter
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

    @Column(name = "category_id")
    private int category; // category

    @JsonIgnore // json 할때 무시하고 json 생성, image에서 product는 mapping용이면 충분
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name="cart_id") //OrderItem은 하나의 Order만 가진다. => order_id 매핑
    private Cart cart;
}
