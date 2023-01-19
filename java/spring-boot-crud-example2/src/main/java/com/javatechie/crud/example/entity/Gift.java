package com.javatechie.crud.example.entity;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@Setter
@Getter
@RequiredArgsConstructor
@Entity
@Table(name = "gift")
public class Gift {
    @Id
    @GeneratedValue
    @Column(name = "gift_id")
    private int id;

    @OneToMany(mappedBy="gift")
    private List<GiftItem> giftItems = new ArrayList<>();;

    private int totPrice;

}
