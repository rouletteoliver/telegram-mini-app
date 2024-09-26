import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import kotlinx.browser.document
import org.jetbrains.compose.web.renderComposable

fun main() {
    renderComposable(rootElementId = "root") {
        App()
    }
}

@Composable
fun App() {
    MaterialTheme {
        Column(
            modifier = Modifier.fillMaxSize().padding(16.dp),
            verticalArrangement = Arrangement.Top,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Header()
            Spacer(modifier = Modifier.height(20.dp))
            BalanceSection()
            Spacer(modifier = Modifier.height(20.dp))
            ProfileDetails()
            Spacer(modifier = Modifier.height(20.dp))
            ConnectButton()
        }
    }
}

@Composable
fun Header() {
    Row(
        horizontalArrangement = Arrangement.SpaceBetween,
        modifier = Modifier.fillMaxWidth()
    ) {
        Button(onClick = { /* Логика для поиска */ }) {
            Text("search game")
        }
        Button(onClick = { /* Логика для игры */ }) {
            Text("game")
        }
        Button(onClick = { /* Логика для профиля */ }) {
            Text("profile")
        }
    }
}

@Composable
fun BalanceSection() {
    Text("Баланс: 100", style = MaterialTheme.typography.h5)
    Text("0x121f32wef22231r2w1rrer77rrgg", style = MaterialTheme.typography.body1)
}

@Composable
fun ProfileDetails() {
    Row(
        horizontalArrangement = Arrangement.SpaceBetween,
        modifier = Modifier.fillMaxWidth()
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            Text("nickname")
            Box(modifier = Modifier.size(60.dp).background(MaterialTheme.colorScheme.primary)) {
                // Placeholder для аватара
            }
        }
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            Text("winrate")
            Text("0%") // Placeholder для Winrate
        }
    }
}

@Composable
fun ConnectButton() {
    Button(onClick = { /* Логика подключения EVM */ }) {
        Text("connect evm")
    }
}
