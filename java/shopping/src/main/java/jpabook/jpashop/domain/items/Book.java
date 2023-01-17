package jpabook.jpashop.domain.items;

import jpabook.jpashop.dto.ItemForm;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.DiscriminatorValue;
import javax.persistence.Entity;

@Entity
@Getter
@Setter
@DiscriminatorValue("B") // single table 이라 저장시 구분용
public class Book extends Item {
    private String author;
    private String isbn;

    @Override
    public Item createItem(ItemForm itemForm) {
        this.setName(itemForm.getName());
        this.setPrice(itemForm.getPrice());
        this.setStockQuantity(itemForm.getStockQuantity());
        this.setIsbn(itemForm.getIsbn());
        this.setAuthor(itemForm.getAuthor());
        return this;
    }

    @Override
    public ItemForm transItemForm() {
        Book book = (Book) this;

        ItemForm itemForm = new ItemForm();
        itemForm.setDtype(book.getDtype());
        itemForm.setId(book.getId());
        itemForm.setName(book.getName());
        itemForm.setPrice(book.getPrice());
        itemForm.setStockQuantity(book.getStockQuantity());

        itemForm.setAuthor(book.getAuthor());
        itemForm.setIsbn(book.getIsbn());

        return itemForm;
    }
}
