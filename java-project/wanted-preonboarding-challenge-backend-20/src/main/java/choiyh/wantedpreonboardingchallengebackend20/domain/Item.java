package choiyh.wantedpreonboardingchallengebackend20.domain;

import jakarta.persistence.*;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;

import java.sql.Timestamp;

@Getter
@Setter
@Entity
@Table(name = "wanted_item")
public class Item {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private Integer price;

    public enum Status {
        Sale,
        Reserved,
        Completed
    }

    private Status status;

    private Timestamp createdAt;
    private Timestamp updatedAt;

    @ManyToOne
    private User seller;

    @OneToOne
    private User buyer;
}
