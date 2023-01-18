package com.javatechie.crud.example.controller;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.javatechie.crud.example.common.CommonMethods;
import com.javatechie.crud.example.entity.Img;
import com.javatechie.crud.example.entity.Product;
import com.javatechie.crud.example.repository.ProductRepository;
import com.javatechie.crud.example.service.ImgService;
import com.javatechie.crud.example.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequiredArgsConstructor
public class ProductController {

    private final ProductService productService;
    private final ImgService imgService;
    ObjectMapper objectMapper = new ObjectMapper();
    private final ProductRepository productRepository;

//    @PostMapping("/addproduct")
//    public Product addProduct(@RequestBody Product product) {
//        return productService.saveProduct(product);
//    }

    //https://devjaewoo.tistory.com/88 error 참고.
    @PostMapping("/addproduct")
    public Product test(@RequestBody String message) throws Exception {
        return productService.createProduct(message);
    }
    @PostMapping("/addproducts") //여러개 한번에 찜하진 않을듯.
    public List<Product> addProducts(@RequestBody String messages) throws Exception {
        TypeReference<Map<String, String>> typeReference = new TypeReference<Map<String,String>>() {};
        Map<String, String> map = objectMapper.readValue(messages, typeReference);
        List<Product> products = new ArrayList<Product>();
        for (int i = 0; i < map.size(); i++) {
            products.add(productService.createProduct(map.get(String.valueOf(i))) );
        };

        return products;
    }

    @GetMapping("/products")
    public List<Product> getProducts() {
        return productService.getProducts();
    }

//    @GetMapping("/product/{id}")
//    public Product findProductById(@PathVariable int id) {
//        return productService.getProductById(id);
//    }

    @GetMapping("/product/{text}")
    public Product findProductByName(@PathVariable String text) {
        // text.chars().allMatch(Character::isDigit); 이렇게 boolean 반환 받기도 가능
        try {
            Double.parseDouble(text);//숫자면
            return productService.getProductById(Integer.parseInt(text));
        } catch (NumberFormatException e) {
            return productService.getProductByName(text);
        }

    }

    @PutMapping("/update")
    public Product updateProduct(@RequestBody Product product) {
        return productService.updateProduct(product);
    }

    @DeleteMapping("/delete/{id}")
    public String deleteProduct(@PathVariable int id) {
        return productService.deleteProduct(id);
    }

}