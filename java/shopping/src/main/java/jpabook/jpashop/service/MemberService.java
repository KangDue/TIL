package jpabook.jpashop.service;

import jpabook.jpashop.domain.Member;
import jpabook.jpashop.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional(readOnly = true) // 읽기 성능 최적화
@RequiredArgsConstructor
public class MemberService {
     // memberRepository 를 인젝션 해줌.
    private final MemberRepository memberRepository;

    @Transactional // 기본적으로 이안에서 data 변경해야함. spring꺼로 쓰자
    public Long join(Member member) {
        validateDuplicateMember(member);
        memberRepository.save(member);
        return member.getId();
    }

    public void validateDuplicateMember(Member member) {
        List<Member> findMembers = memberRepository.findByName(member.getName());
        if (!findMembers.isEmpty()) {
            throw new IllegalStateException("이미 존재하는 회원입니다.");
        }
    }


    public Member findOne(Long memberId) {
        return memberRepository.findOne(memberId);
    }
}
