package jpabook.jpashop.repository;

import jpabook.jpashop.domain.items.Item;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import java.util.List;

@Repository
@RequiredArgsConstructor
public class ItemRepository {

    private final EntityManager em;

    public void save(Item item) {
        if (item.getId() == null) { // 새로만든 객체
            em.persist(item);
        } else { // db 에있는 객체, update와 비슷한 의미
            em.merge(item);
        }
    }

    public Item findOne(Long id) {
        return em.find(Item.class,id);
    }

    public List<Item> findAll() {
        return em.createQuery("SELECT i FROM Item i", Item.class).getResultList();
    }
}
