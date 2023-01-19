package com.javatechie.crud.example.service;

import com.javatechie.crud.example.entity.Gift;
import com.javatechie.crud.example.entity.GiftItem;
import com.javatechie.crud.example.entity.Product;
import com.javatechie.crud.example.repository.GiftItemRepository;
import lombok.RequiredArgsConstructor;
import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Iterator;

@Service
@RequiredArgsConstructor
public class GiftItemService {
    private final GiftItemRepository giftItemRepository;
    private final ProductService productService;
    public GiftItem saveGiftItem(GiftItem cartItem) {
        return giftItemRepository.save(cartItem);
    }
    @Transactional
    public GiftItem createGiftItem(Product product, Gift gift, Integer quantity, String options) throws JSONException {
        GiftItem giftItem = new GiftItem();
        JSONObject jObj = new JSONObject(options);
        Integer price = product.getPrice();
        for (Iterator it = jObj.keys(); it.hasNext(); ) {
            System.out.println(it.next());
            price += jObj.getInt((String) it.next());
        }
        giftItem.setProduct(product);
        giftItem.setGift(gift);
        giftItem.setQuantity(quantity);
        giftItem.setOptions(options);
        giftItem.setPurePrice(price*quantity);
        return giftItemRepository.save(giftItem);
    }


//    public List<Cart> saveCarts(List<Cart> carts) {
//        return cartRepository.saveAll(carts);
//    }
//
//    public List<Cart> getCarts() {
//        return cartRepository.findAll();
//    }

    public GiftItem getGiftItemById(int id) {
        return giftItemRepository.findById(id).orElse(null);
    }
    public String deleteGiftItem(int id) {
        giftItemRepository.deleteById(id);
        return "Item removed !!" + id;
    }

}
