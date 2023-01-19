package com.javatechie.crud.example.controller;


import com.javatechie.crud.example.entity.Cart;
import com.javatechie.crud.example.entity.Gift;
import com.javatechie.crud.example.service.*;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequiredArgsConstructor
public class GiftController {

    private final ProductService productService;
    private final ImgService imgService;
    private final GiftService giftService;
    private final GiftItemService giftItemService;

    @PostMapping("/create-empty-gift")
    public Gift gift(@RequestBody Gift gift) throws Exception {
        return giftService.saveGift(gift);
    }

    @PostMapping("/add-to-gift")
    public Gift addToGift(@RequestBody String message) throws Exception {
        return giftService.addGiftItem(message);
    }

    // 장바구니에서 단일 품목으로 wish 생성
    @GetMapping("/cart/{itemId}/makewish")
    public String makeWish(@RequestParam(value = "itemId", required = true) String itemId) throws Exception {
        Gift gift = new Gift();
        return "1";
    }
}
