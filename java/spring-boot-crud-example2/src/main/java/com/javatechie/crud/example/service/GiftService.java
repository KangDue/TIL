package com.javatechie.crud.example.service;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.javatechie.crud.example.entity.*;
import com.javatechie.crud.example.repository.CartRepository;
import com.javatechie.crud.example.repository.GiftRepository;
import lombok.RequiredArgsConstructor;
import org.json.JSONObject;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class GiftService {
    private final GiftRepository giftRepository;
    private final ProductService productService;
    private final GiftItemService giftItemService;
    ObjectMapper objectMapper = new ObjectMapper();

    public Gift saveGift(Gift gift) {
        return giftRepository.save(gift);
    }

//    public List<Cart> saveCarts(List<Cart> carts) {
//        return cartRepository.saveAll(carts);
//    }
//
//    public List<Cart> getCarts() {
//        return cartRepository.findAll();
//    }

    public Gift getGiftById(int id) {
        return giftRepository.findById(id).orElse(null);
    }
    public String deleteGift(int id) {
        giftRepository.deleteById(id);
        return "gift removed !!" + id;
    }

    public Gift addGiftItem(String message) throws Exception {
//        TypeReference<Map<String, String>> typeReference = new TypeReference<Map<String,String>>() {};
//        Map<String, String> map = objectMapper.readValue(message, typeReference);
        JSONObject map = new JSONObject(message);
        Gift gift =  getGiftById(Integer.parseInt(map.getString("giftId")));
        Product product = productService.getProductById(Integer.parseInt(map.getString("productId")));
        GiftItem giftItem = giftItemService.createGiftItem(product, gift, Integer.parseInt(map.getString("quantity")), map.getString("options"));
        Integer price = (int) (giftItem.getPurePrice()*1.03/10*10);

        List<GiftItem> giftItems = gift.getGiftItems();
        giftItems.add(giftItem);
        gift.setTotPrice(gift.getTotPrice() + price);
        gift.setGiftItems(giftItems);
        return saveGift(gift);
    }
}
