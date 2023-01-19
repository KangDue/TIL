package com.javatechie.crud.example.repository;

import com.javatechie.crud.example.entity.CartItem;
import com.javatechie.crud.example.entity.GiftItem;
import org.springframework.data.jpa.repository.JpaRepository;

public interface GiftItemRepository extends JpaRepository<GiftItem, Integer> {
}
