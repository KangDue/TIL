package jpabook.jpashop.domain;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter
@Setter
@Table(name="orders") // 이름 설정한 table
public class Order {

    @Id @GeneratedValue
    @Column(name = "order_id")
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY) //관계 설정 잘하자!
    @JoinColumn(name = "member_id") //mapping을 뭐로하냐 ?
    private Member member;

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL)
    private List<OrderItem> orderItems = new ArrayList<>();

    // Order의 delivery가 연관관계의 주인이됨.
    @OneToOne(fetch = FetchType.LAZY, cascade = CascadeType.ALL) // 1대1 은 fk 위치가 자유라, 자주 조회하는 곳에 위치시키기 추천
    @JoinColumn(name = "delivery_id")
    private Delivery delivery;

    private LocalDateTime orderDate;

    @Enumerated(EnumType.STRING)
    private OrderStatus status; // [ORDER, CANCEL]

    //연관관계 method
    //양방향 관계일때 황요하기 좋음. 한쪽만 주인설정해도 반대에서 보기용
    public void setMember(Member member) {
        this.member = member;
        member.getOrders().add(this);
    }

    public void addOrderItem(OrderItem orderItem) {
        orderItems.add(orderItem);
        orderItem.setOrder(this);
    }

    public void setDelivery(Delivery delivery) {
        this.delivery = delivery;
        delivery.setOrder(this);
    }
}
