package iua.kaf.Backend.model.business;

import java.util.List;

import iua.kaf.Backend.model.Usuario;
import iua.kaf.Backend.model.business.exception.BusinessException;
import iua.kaf.Backend.model.business.exception.FoundException;
import iua.kaf.Backend.model.business.exception.NotFoundException;

public interface IUsuarioBusiness {
    
    public Usuario load(long id) throws NotFoundException, BusinessException;

    public Usuario load(String nombre) throws NotFoundException, BusinessException;
    public List<Usuario> list() throws BusinessException;

    public Usuario add(Usuario cliente) throws FoundException, BusinessException;

    public void delete(long id) throws NotFoundException, BusinessException;


}
