package com.javatechie.crud.example.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Setter
@Getter
@RequiredArgsConstructor
@Entity
@Table(name = "gift_item")
public class GiftItem {
    @Id
    @GeneratedValue
    @Column(name = "item_id")
    private int id;
    @OneToOne
    @JoinColumn(name = "product_id")
    private Product product;

    @JsonIgnore // json 할때 무시하고 json 생성, image에서 product는 mapping용이면 충분
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name="gift_id") //OrderItem은 하나의 Order만 가진다. => order_id 매핑
    private Gift gift;

    private int quantity; // 수량
    private String options; // json 형태
    private int purePrice; // 상품 가격(수량 옵션)
    //state
}
