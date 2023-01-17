package com.javatechie.crud.example.controller;

import com.javatechie.crud.example.entity.Product;
import com.javatechie.crud.example.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class ProductController {

    private final ProductService productService;

    @PostMapping("/addproduct")
    public Product addProduct(@RequestBody Product product) {
        return productService.saveProduct(product);
    }
    @PostMapping("/addproducts")
    public List<Product> addProducts(@RequestBody List<Product> products) {
        return productService.saveProducts(products);
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
