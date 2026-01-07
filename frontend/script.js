const API_URL = 'http://localhost:5000/api/vagas';

const vagasContainer = document.getElementById('vagas-container');
const inputBusca = document.getElementById('busca');
const selectPlataforma = document.getElementById('filtroPlataforma');
const btnLimpar = document.getElementById('btnLimpar');

let todasAsVagas = [];

async function carregarVagas() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();
        todasAsVagas = data;
        exibirVagas(todasAsVagas);
    } catch (error) {
        console.error('Erro ao carregar vagas:', error);
        vagasContainer.innerHTML = `
            <div class="col-12">
                <p class="text-center text-danger py-5">
                    ❌ Erro ao carregar as vagas. Verifique se o backend está rodando.
                </p>
            </div>
        `;
    }
}

function exibirVagas(vagas) {
    if (vagas.length === 0) {
        vagasContainer.innerHTML = `
            <div class="col-12">
                <p class="text-center text-muted py-5">
                    📭 Nenhuma vaga encontrada com esses filtros.
                </p>
            </div>
        `;
        return;
    }

    vagasContainer.innerHTML = vagas.map(vaga => `
        <div class="col-12 col-sm-6 col-lg-4">
            <div class="vaga-card">
                <span class="vaga-plataforma">${vaga.plataforma}</span>
                <h5 class="vaga-titulo">${vaga.titulo}</h5>
                <p class="vaga-preco">${vaga.preco}</p>
                <p class="vaga-descricao">${vaga.descricao}</p>
                <p class="vaga-data">📅 ${formatarData(vaga.data)}</p>
            </div>
        </div>
    `).join('');
}

function filtrarVagas() {
    const textoBusca = inputBusca.value.toLowerCase();
    const plataforma = selectPlataforma.value;

    const vagasFiltradas = todasAsVagas.filter(vaga => {
        const matchBusca = 
            vaga.titulo.toLowerCase().includes(textoBusca) ||
            vaga.descricao.toLowerCase().includes(textoBusca) ||
            vaga.plataforma.toLowerCase().includes(textoBusca);
        
        const matchPlataforma = plataforma === '' || vaga.plataforma === plataforma;

        return matchBusca && matchPlataforma;
    });

    exibirVagas(vagasFiltradas);
}

function formatarData(data) {
    const date = new Date(data);
    return date.toLocaleDateString('pt-BR');
}

function limparFiltros() {
    inputBusca.value = '';
    selectPlataforma.value = '';
    exibirVagas(todasAsVagas);
}

inputBusca.addEventListener('input', filtrarVagas);
selectPlataforma.addEventListener('change', filtrarVagas);
btnLimpar.addEventListener('click', limparFiltros);

document.addEventListener('DOMContentLoaded', carregarVagas);