package jpabook.jpashop.domain;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;



@Entity
@Getter
@Setter
public class Member {
    @Id
    @GeneratedValue
    @Column(name = "member_id") // 컬럼명 지정
    private Long id;

    private String name;

    @Embedded // embeddable 은 이렇게 해주는게 좋음. 한쪽만 해도 되긴함.
    private Address address;

    // mappedBy로 종속된 녀석임을 나타냄. 그저 read용 , 거울일 뿐
    @OneToMany(mappedBy = "member", cascade = CascadeType.ALL)
    private List<Order> orders = new ArrayList<Order>();


}
