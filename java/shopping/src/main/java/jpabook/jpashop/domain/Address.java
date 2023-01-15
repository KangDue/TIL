package jpabook.jpashop.domain;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.Embeddable;

@Embeddable // 내장 타입 , 어떤 table에 내장
@Getter @Setter
public class Address {
    private String city;
    private String street;
    private String zipCode;

    protected Address() {} // jpa 스펙상 생성자는 default 생성자 또는 public , protected 만 허용

    public Address(String city, String street, String zipCode) {
        this.city = city;
        this.street = street;
        this.zipCode = zipCode;
    }

}
