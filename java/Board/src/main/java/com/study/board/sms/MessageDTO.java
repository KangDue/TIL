package com.study.board.sms;

import lombok.*;

@AllArgsConstructor
@NoArgsConstructor
@Setter
@Getter
@Builder
public class MessageDTO {
    String to;
    String content;
}
