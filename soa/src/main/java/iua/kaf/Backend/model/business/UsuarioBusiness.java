package iua.kaf.Backend.model.business;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import iua.kaf.Backend.model.Usuario;
import iua.kaf.Backend.model.business.exception.BusinessException;
import iua.kaf.Backend.model.business.exception.FoundException;
import iua.kaf.Backend.model.business.exception.NotFoundException;
import iua.kaf.Backend.model.persistence.UsuarioRepository;
import lombok.extern.slf4j.Slf4j;

@Service
@Slf4j
public class UsuarioBusiness implements IUsuarioBusiness{
    
    private UsuarioRepository usuarioDAO;

    @Override
    public Usuario load(long id) throws NotFoundException, BusinessException {
        Optional<Usuario> r;
    try {
      r = usuarioDAO.findById(id);
    } catch (Exception e) {
      log.error(e.getMessage(), e);
      throw BusinessException.builder().ex(e).build();
    }
    if (r.isEmpty()) {
      throw NotFoundException.builder().message("No se encuentra el usuario con id=" + id).build();
    }

    return r.get();
    }

    @Override
    public Usuario load(String nombre) throws NotFoundException, BusinessException {
          Optional<Usuario> r;
    try {
      r = usuarioDAO.findByNombre(nombre);
    } catch (Exception e) {
      log.error(e.getMessage(), e);
      throw BusinessException.builder().ex(e).build();
    }
    if (r.isEmpty()) {
      throw NotFoundException.builder().message("No se encuentra el usuario con nombre=" + nombre).build();
    }

    return r.get();
    }

    @Override
    public List<Usuario> list() throws BusinessException {
        try {
            return usuarioDAO.findAll();
          } catch (Exception e) {
            log.error(e.getMessage(), e);
            throw BusinessException.builder().ex(e).build();
          }
    }

    @Override
    public Usuario add(Usuario usuario) throws FoundException, BusinessException {
        try {
            load(usuario.getId());
            throw FoundException.builder().message("Se encuentró el usuario con id=" + usuario.getId()).build();
          } catch (NotFoundException e) {
          }
      
          try {
            return usuarioDAO.save(usuario);
          } catch (Exception e) {
            log.error(e.getMessage(), e);
            throw BusinessException.builder().ex(e).build();
          }
    }

    @Override
    public void delete(long id) throws NotFoundException, BusinessException {
        load(id);
    try {
      usuarioDAO.deleteById(id);
    } catch (Exception e) {
      log.error(e.getMessage(), e);
      throw BusinessException.builder().ex(e).build();
    }
    }
    
}
