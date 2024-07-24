package choiyh.wantedpreonboardingchallengebackend20.domain;

import jakarta.persistence.*;

import java.sql.Timestamp;

@Entity
@Table(name = "wanted_user")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String email;

    private Timestamp createdAt;
    private Timestamp modifiedAt;

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public Timestamp getCreatedAt() {
        return createdAt;
    }

    public Timestamp getModifiedAt() {
        return modifiedAt;
    }
}
