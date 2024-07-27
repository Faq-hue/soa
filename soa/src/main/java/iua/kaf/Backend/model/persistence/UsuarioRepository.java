package iua.kaf.Backend.model.persistence;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import iua.kaf.Backend.model.Usuario;

@Repository
public interface UsuarioRepository extends JpaRepository<Usuario, Long>{

    public Optional<Usuario> findByNombre(String nombre);
    
    public Optional<Usuario> findById(Long id);

}
    
