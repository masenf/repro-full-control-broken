import pynecone as pc

config = pc.Config(
    app_name="repro_full_control_broken",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
