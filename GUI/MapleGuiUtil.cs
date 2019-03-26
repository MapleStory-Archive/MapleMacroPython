using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MapleAssistToolPy
{
	class MapleGuiUtil
	{

		public void execStartUp(bool execMode,string macroName)
		{
			
			StopButton stopButton = new StopButton(macroName);
			settingStopButton(stopButton);
			stopButton.Show();

			execScript(execMode);

		}

		public void settingStopButton(StopButton stopButton)
		{
			stopButton.Left = 800;
			stopButton.Top = 800;
			stopButton.StartPosition = FormStartPosition.Manual;
		}

		public int execScript(bool execMode)
		{

			string pythonCmd = @"python ..\MapleMacroPy\ScriptExecutor.py";

			#if DEBUG
				pythonCmd = @"python ScriptExecutor.py";
			#endif

			if (execMode)
			{
				pythonCmd += " UWSC";
			}
			else
			{
				pythonCmd += " PY";
			}

			// プロセスクラスのインスタンス化
			var p = new Process();

			// cmd.exeのパスを取得
			p.StartInfo.FileName = System.Environment.GetEnvironmentVariable("ComSpec");
			// 出力を読み取れるようにする
			p.StartInfo.UseShellExecute = false;
			p.StartInfo.RedirectStandardOutput = true;
			p.StartInfo.RedirectStandardInput = false;
			// ウインドウを表示しないようにする
			p.StartInfo.CreateNoWindow = true;
			// hello.pyを実行する
			p.StartInfo.Arguments = @"/c cd C:\Users\test\Desktop\MapleMacroPy";

			// 起動
			p.Start();
			p.StartInfo.Arguments = @"/c " + pythonCmd;
			p.Start();
			string results = p.StandardOutput.ReadToEnd();
			Console.Write(results);




			return 0;
		}
	}
}