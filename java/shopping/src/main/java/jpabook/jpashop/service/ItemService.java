package jpabook.jpashop.service;

import jpabook.jpashop.domain.items.Item;
import jpabook.jpashop.repository.ItemRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional(readOnly = true)
@RequiredArgsConstructor
public class ItemService {
    private final ItemRepository itemRepository;

    // 경우에 따라서 컨트롤 repo에 바로접근하는 방식도 고려해 볼만함
    public void saveItem(Item item) {
        itemRepository.save(item);
    }

    @Transactional
    public List<Item> findItems() {
        return itemRepository.findAll();
    }

    public Item findOne(Long itemId) {
        return itemRepository.findOne(itemId);
    }

}
