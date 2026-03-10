function adicionarDespesa() 
    //adicionar
    {
    var campoDesc = document.getElementById('descricao');
    var campoVal = document.getElementById('valor');
    var campoData = document.getElementById('dataVencimento');
    var campoCategoria = document.getElementById('categoria');

    //salvar 
    var descricao = campoDesc.value;
    var valor = parseFloat(campoVal.value);
    var dataVencimento = campoData.value;
    var categoria = campoCategoria.value;

    //validação
    if (descricao === '' || isNaN(valor) || dataVencimento === ''|| categoria === '') {
        alert('Por favor, preencha todos os campos corretamente.');
        return;
    
   
    }
    // condição
    var idTabelaAlvo ;
    if (categoria === 'contasBasicas') {
        idTabelaAlvo = 'contasBasicas';
    } else if (categoria === 'saude') {
        idTabelaAlvo = 'saude';
    } else if (categoria === 'cartao') {
        idTabelaAlvo = 'cartao';
    } else if (categoria === 'gerais') {
        idTabelaAlvo = 'gerais';
    }
    
    //    Edição    


    // data formatada
    var dataFormatada = dayjs(dataVencimento).format('DD/MM/YYYY');
    // inserir dados na tabela
    var corpoTabela = document.getElementById(idTabelaAlvo).getElementsByTagName('tbody');
    var novaLinha = corpoTabela[0].insertRow();

    novaLinha.insertCell(0).innerHTML = descricao;
    novaLinha.insertCell(1).innerHTML = 'R$ '  + valor.toFixed(2);
   // novaLinha.insertCell(2).innerHTML = categoria.charAt(0).toUpperCase() + categoria.slice(1);
    novaLinha.insertCell(2).innerHTML = dataFormatada;
    //limpar campos
    campoDesc.value = '';
    campoVal.value = '';
    campoData.value = '';
    campoCategoria.value = '';
}
function edicao(id, descricao, valor, dataVencimento, categoria) {
    document.getElementById('edit_id').value = id;
    document.getElementById('descricao').value = descricao;
    document.getElementById('valor').value = valor;
    document.getElementById('dataVencimento').value = dataVencimento;
    document.getElementById('categoria').value = categoria;
    // Exibir botões de editar e excluir, ocultar botão de adicionar
    document.getElementById('btnEditar').style.display = 'inline-block';
    document.getElementById('btnExcluir').style.display = 'inline-block';
    document.getElementById('btnAdicionar').style.display = 'none';
}
//botão excluir
function abrirModalExcluir() {
    document.getElementById('modalExcluir').style.display = 'flex';
}
function fecharModalExcluir() {
    document.getElementById('modalExcluir').style.display = 'none';
}
document.addEventListener('keydown', function(event) {
    var modal = document.getElementById('modalExcluir');
    if (modal.style.display === 'flex' && event.key === 'Escape') {
        fecharModalExcluir();
    }
        if (event.key === 'Enter') {
            event.preventDefault();
            confirmarExclusao();
        }
});
function confirmarExclusao() {
        var form = document.getElementById('adicionarDespesa');
                form.action = '/excluir_despesa';
                form.method = 'POST';
                form.submit();
                fecharModalExcluir();
}

