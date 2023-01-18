package com.javatechie.crud.example.service;

import com.javatechie.crud.example.entity.Cart;
import com.javatechie.crud.example.entity.Img;
import com.javatechie.crud.example.repository.CartRepository;
import com.javatechie.crud.example.repository.ImgRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class CartService {
    private final CartRepository cartRepository;

    public Cart saveCart(Cart cart) {
        return cartRepository.save(cart);
    }

//    public List<Cart> saveCarts(List<Cart> carts) {
//        return cartRepository.saveAll(carts);
//    }
//
//    public List<Cart> getCarts() {
//        return cartRepository.findAll();
//    }

    public Cart getCartById(int id) {
        return cartRepository.findById(id).orElse(null);
    }
    public String deleteCart(int id) {
        cartRepository.deleteById(id);
        return "img removed !!" + id;
    }

}
