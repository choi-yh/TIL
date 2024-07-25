package choiyh.wantedpreonboardingchallengebackend20.domain;

import jakarta.persistence.*;

import java.sql.Timestamp;

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

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Integer getPrice() {
        return price;
    }

    public Status getStatus() {
        return status;
    }

    public Timestamp getCreatedAt() {
        return createdAt;
    }

    public Timestamp getUpdatedAt() {
        return updatedAt;
    }

    public User getSeller() {
        return seller;
    }
}
