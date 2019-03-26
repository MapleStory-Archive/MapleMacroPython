using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MapleAssistToolPy
{
	public partial class StopButton : Form
	{
		public StopButton(string macroName)
		{
			InitializeComponent();
			this.execMacroName.Text = macroName;
		}

		private void Stop_Click(object sender, EventArgs e)
		{
			int ret = stopScript();

			if (ret != 0)
			{
				//error
			}
			
			//stop画面を閉じる
			this.Close();
		}

		public int stopScript()
		{
			return 0;
		}
	}
}
