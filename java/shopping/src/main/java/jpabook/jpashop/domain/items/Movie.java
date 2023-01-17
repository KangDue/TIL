package jpabook.jpashop.domain.items;

import jpabook.jpashop.dto.ItemForm;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.DiscriminatorValue;
import javax.persistence.Entity;

@Entity
@Getter
@Setter
@DiscriminatorValue("M") // single table 이라 저장시 구분용
public class Movie extends Item {
    private String director;
    private String actor;

    @Override
    public Item createItem(ItemForm itemForm) {
        this.setName(itemForm.getName());
        this.setPrice(itemForm.getPrice());
        this.setStockQuantity(itemForm.getStockQuantity());
        this.setDirector(itemForm.getDirector());
        this.setActor(itemForm.getActor());
        return this;
    }

    @Override
    public ItemForm transItemForm() {
        Movie movie = (Movie) this;
        ItemForm itemForm = new ItemForm();
        itemForm.setDtype(movie.getDtype());
        itemForm.setId(movie.getId());
        itemForm.setName(movie.getName());
        itemForm.setPrice(movie.getPrice());
        itemForm.setStockQuantity(movie.getStockQuantity());

        itemForm.setDirector(movie.getDirector());
        itemForm.setActor(movie.getActor());

        return itemForm;
    }
}
