import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

st.set_page_config(
    page_title="Analisador de Arquivos",
    layout="wide"
)

st.title("📊 Analisador de Arquivos CSV / Excel")

@st.cache_data(show_spinner=False)
def load_data(file, ext):
    if ext == "csv":
        return pd.read_csv(file, low_memory=False)
    return pd.read_excel(file)

uploaded_file = st.file_uploader(
    "📂 Faça upload de um arquivo CSV ou Excel",
    type=["csv", "xls", "xlsx"],
    key="uploader_principal"
)


if uploaded_file is not None:
    ext = uploaded_file.name.split(".")[-1].lower()

    try:
        with st.spinner("Carregando arquivo..."):
            df = load_data(uploaded_file, ext)
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        st.stop()

    st.success(f"Arquivo carregado • {df.shape[0]} linhas x {df.shape[1]} colunas")

 
    st.subheader("🔍 Filtro por palavra-chave")
    keyword = st.text_input(
        "Digite uma palavra ou número para buscar em todas as colunas",
        key="keyword_input"
    )

    if keyword:
        df_filtrado = df[
            df.astype(str)
              .apply(lambda row: row.str.contains(keyword, case=False, na=False).any(), axis=1)
        ]
    else:
        df_filtrado = df

    st.write(f"Linhas após filtro: **{len(df_filtrado)}**")

   
    st.subheader("👀 Pré-visualização")
    st.dataframe(df_filtrado.head(200), use_container_width=True)

  
    st.subheader("📈 Estatísticas")
    st.dataframe(df_filtrado.describe(include="all"), use_container_width=True)


    st.subheader("⚠️ Valores faltantes")
    st.dataframe(
        df_filtrado.isnull().sum().to_frame("Qtd Nulos"),
        use_container_width=True
    )


    st.subheader("📊 Visualizações")

    numeric_cols = df_filtrado.select_dtypes(include=["number"]).columns
    cat_cols = df_filtrado.select_dtypes(include=["object", "category"]).columns

    col1, col2 = st.columns(2)

    with col1:
        if len(numeric_cols) > 0:
            num_col = st.selectbox(
                "Coluna numérica",
                numeric_cols,
                key="num_col_select"
            )
            fig, ax = plt.subplots()
            sns.histplot(df_filtrado[num_col].dropna(), kde=True, ax=ax)
            st.pyplot(fig)
        else:
            st.info("Nenhuma coluna numérica encontrada")

    with col2:
        if len(cat_cols) > 0:
            cat_col = st.selectbox(
                "Coluna categórica",
                cat_cols,
                key="cat_col_select"
            )
            fig, ax = plt.subplots()
            sns.countplot(data=df_filtrado, x=cat_col, ax=ax)
            plt.xticks(rotation=45)
            st.pyp
