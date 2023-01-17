package jpabook.jpashop.domain;


import jpabook.jpashop.domain.items.Item;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter @Setter
public class OrderItem {

    @Id @GeneratedValue
    @Column(name = "order_item_id")
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY) // 모든 order가 table 하나에 쌓여감. -> 테이블상 여러개의 orderItem이 하나의 item 가리킬 수 있다.
    @JoinColumn(name = "item_id") // order_item이 주인인 1대 다 관계
    private Item item;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "order_id") // order_item이 주인인 1대 다 관계
    private Order order;

    private int orderPrice;

    private int count;

    protected OrderItem() {} // @NoArgsConstructor(access=AccessLevel.PROTECTED)
    public static OrderItem createOrderItem(Item item, int orderPrice, int count) {
        OrderItem orderItem = new OrderItem();
        orderItem.setItem(item);
        orderItem.setOrderPrice(orderPrice);
        orderItem.setCount(count);

        item.removeStock(count);
        return orderItem;
    }

    // B-logic
    public void cancel() {
        getItem().addStock(count);
    }

    public int getTotalPrice() {
        return getOrderPrice() * getCount();
    }

}
