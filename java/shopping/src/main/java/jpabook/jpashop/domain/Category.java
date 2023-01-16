package jpabook.jpashop.domain;

import jpabook.jpashop.domain.items.Item;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter @Setter
public class Category {

    @Id
    @GeneratedValue
    @Column(name = "category_id")
    private Long id;

    private String name;


    @ManyToMany
    @JoinTable(name = "category_item",
        joinColumns = @JoinColumn(name = "category_id"), //중개 table의 컬럼
            inverseJoinColumns = @JoinColumn(name = "item_id")) // item 쪽으로 들어가는 id
    private List<Item> items = new ArrayList<>();

    // self 참고 , 댓글 대댓글 느낌, 또는 유저에서 팔로워, 팔로우
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "parent_id")
    private Category parent;

    @OneToMany(mappedBy = "parent", fetch = FetchType.LAZY)
    private List<Category> child = new ArrayList<>();

    // relationship convenience methods
    public void addChildCategory(Category child) {
        this.child.add(child);//컬렉션에서도 추가되야함
        child.setParent(this);//자식도 부모가 누군지 알아야함.
    }
}
