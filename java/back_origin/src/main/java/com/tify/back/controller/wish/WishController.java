package com.tify.back.controller.wish;
import com.tify.back.dto.wish.AddWishDto;
import com.tify.back.model.wish.Wish;
import com.tify.back.repository.wish.WishRepository;
import com.tify.back.service.wish.WishService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/wish")
public class WishController {
    private final WishService wishService;
    private final WishRepository wishRepository;
    @PostMapping("/add")
    public Integer addWish(@RequestBody AddWishDto dto){

        //유효성 검사
        if(dto.getWishTitle().equals(""))
        {
            // 타이틀이 입력되지않았을때
            return 3;
        }

        boolean result = wishService.saveWish(dto);

        if(result)
        {
            return 0;
        }else {
            return 1;
        }
    }
    @GetMapping("/detail")
    public Wish wishList(@RequestParam(value = "wishId", required = true) Long wishId){
        return wishService.wishDetailId(wishId);
    }
    @GetMapping
    public List<Wish> Wish() {
        return wishRepository.findAll();
    }

}