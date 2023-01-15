package jpabook.jpashop;

import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

// entity 찾아주는 놈
@Repository
public class MemberOriginRepository {

    @PersistenceContext
    private EntityManager em;

    public Long save(MemberOrigin member) {
        em.persist(member);
        return member.getId();
    }

    public MemberOrigin find (Long id) {
        return em.find(MemberOrigin.class, id);
    }

}
