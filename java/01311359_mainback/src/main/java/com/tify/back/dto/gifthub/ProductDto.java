package com.tify.back.dto.gifthub;

import com.tify.back.model.gifthub.Product;
import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

import static org.hibernate.query.criteria.internal.ValueHandlerFactory.isNumeric;

@Getter
@Setter
public class ProductDto {
    private String name;
    private String repImg;
    private int quantity;
    private String price;
    private String description;
    private String category;
    private int categoryId;
    private int likeCount;
    private List<ImgDto> images;
    private List<ProductOptionDto> options;

    private List<String> categories = Arrays.asList("뷰티", "전자제품", "키친", "의류", "음식", "출산유아", "홈인테리어", "반려동물용품");
    public Product toEntity() {
        Product product = new Product();
        product.setName(this.name);
        product.setRepImg(this.repImg);
        product.setQuantity(this.quantity);
        String herePrice = this.price.replaceAll(",", "");
        herePrice = herePrice.replace("원","");
        if (isNumeric(herePrice)) {
            product.setPrice(Integer.parseInt(herePrice));
        } else {
            Random random = new Random();
            int randomPrice = random.nextInt(200000 - 15000 + 1) + 15000;
            product.setPrice(randomPrice);
        }

        product.setDescription(this.description);

        if (this.category != null) {
            int code = this.categories.indexOf(this.category);
            if (code < 0) {code = 99999;}
            product.setCategory(code);
        }
        else {
            product.setCategory(this.categoryId);
        }
        product.setLikeCount(this.likeCount);
        return product;
    }
}
