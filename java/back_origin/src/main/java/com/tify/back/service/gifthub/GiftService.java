package com.tify.back.service.gifthub;


import com.tify.back.model.gifthub.Gift;
import com.tify.back.model.gifthub.Product;
import com.tify.back.repository.gifthub.GiftRepository;

import com.tify.back.model.wish.Wish;
import lombok.RequiredArgsConstructor;
import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Iterator;

@Service
@RequiredArgsConstructor
public class GiftService {
    private final GiftRepository giftRepository;
    private final ProductService productService;
    public Gift saveGift(Gift gift) {
        return giftRepository.save(gift);
    }
    @Transactional
    public Gift createGift(Product product, Wish wish, Integer quantity, String options) throws JSONException {
        Gift gift = new Gift();
        JSONObject jObj = new JSONObject(options);
        Integer price = product.getPrice();
        for (Iterator it = jObj.keys(); it.hasNext(); ) {
            System.out.println(it.next());
            price += jObj.getInt((String) it.next());
        }
        gift.setProduct(product);
        gift.setWish(wish);
        gift.setQuantity(quantity);
        gift.setOptions(options);
        gift.setPurePrice(price*quantity);
        return giftRepository.save(gift);
    }


//    public List<Cart> saveCarts(List<Cart> carts) {
//        return cartRepository.saveAll(carts);
//    }
//
//    public List<Cart> getCarts() {
//        return cartRepository.findAll();
//    }

    //Long.valueOf(Optional.ofNullable(id).orElse(0L)
    public Gift getGiftById(Long id) {
        return giftRepository.findById(id).orElse(null);
    }
    public String deleteGift(Long id) {
        giftRepository.deleteById(id);
        return "gift removed !!" + id;
    }

}
