package jpabook.jpashop.domain.item;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.DiscriminatorValue;
import javax.persistence.Entity;

@Entity
@Getter
@Setter
@DiscriminatorValue("A") // single table 이라 저장시 구분용
public class Album extends Item{
    private String Artist;
    private String etc;
}
